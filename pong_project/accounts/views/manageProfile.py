import logging
from django.template.loader import render_to_string
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import update_session_auth_hash, logout, get_user_model
from django.utils.translation import gettext as _
from pong_project.decorators import login_required_json

from accounts.forms import UserNameForm, PasswordChangeForm, AvatarUpdateForm, DeleteAccountForm

logger = logging.getLogger(__name__)
User = get_user_model()


@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required_json, name='dispatch')
class ManageProfileView(View):
    """
    Affiche et gère les formulaires de gestion de profil.
    """
    def get(self, request):
        try:
            user = request.user
            profile_form = UserNameForm(instance=user)
            password_form = PasswordChangeForm(user=user)
            avatar_form = AvatarUpdateForm(instance=user)
            delete_form = DeleteAccountForm(user=user)
            
            rendered_html = render_to_string('accounts/gestion_profil.html', {
                'profile_form': profile_form,
                'password_form': password_form,
                'avatar_form': avatar_form,
                'delete_form': delete_form,
                'profile_user': user,
            })
            return JsonResponse({'status': 'success', 'html': rendered_html}, status=200)
        except Exception as e:
            logger.exception("Erreur lors du chargement de la gestion de profil pour l'utilisateur %s: %s", request.user.username, str(e))
            return JsonResponse({'status': 'error', 'message': _("Une erreur interne est survenue.")}, status=500)


@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required_json, name='dispatch')
class ChangeUsernameView(View):
    """
    Permet de changer le nom d'utilisateur.
    """
    def post(self, request):
        try:
            user = request.user
            form = UserNameForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return JsonResponse({
                    'status': 'success', 
                    'message': _("Nom d'utilisateur mis à jour avec succès.")
                }, status=200)
            else:
                error_messages = " ".join([msg for messages in form.errors.values() for msg in messages])
                return JsonResponse({'status': 'error', 'message': error_messages}, status=400)
        except Exception as e:
            logger.exception("Erreur lors du changement de pseudo pour l'utilisateur %s: %s", request.user.username, str(e))
            return JsonResponse({'status': 'error', 'message': _("Une erreur interne est survenue.")}, status=500)


@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required_json, name='dispatch')
class ChangePasswordView(View):
    """
    Gère le changement de mot de passe.
    """
    def post(self, request):
        try:
            user = request.user
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, user)  # Maintien de la session active
                return JsonResponse({
                    'status': 'success', 
                    'message': _('Mot de passe mis à jour avec succès.')
                }, status=200)
            else:
                error_messages = " ".join([msg for messages in form.errors.values() for msg in messages])
                return JsonResponse({'status': 'error', 'message': error_messages}, status=400)
        except Exception as e:
            logger.exception("Erreur lors du changement de mot de passe pour l'utilisateur %s: %s", request.user.username, str(e))
            return JsonResponse({'status': 'error', 'message': _("Une erreur interne est survenue.")}, status=500)


@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required_json, name='dispatch')
class UpdateAvatarView(View):
    """
    Gère la mise à jour de l'avatar.
    """
    def post(self, request):
        try:
            user = request.user
            form = AvatarUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return JsonResponse({
                    'status': 'success', 
                    'message': _('Avatar mis à jour avec succès.')
                }, status=200)
            else:
                error_messages = " ".join([msg for messages in form.errors.values() for msg in messages])
                logger.error("Erreur lors de la mise à jour de l'avatar pour l'utilisateur %s: %s", request.user.username, error_messages)
                return JsonResponse({'status': 'error', 'message': error_messages}, status=400)
        except Exception as e:
            logger.exception("Erreur lors de la mise à jour de l'avatar pour l'utilisateur %s: %s", request.user.username, str(e))
            return JsonResponse({'status': 'error', 'message': _("Une erreur interne est survenue.")}, status=500)


@method_decorator(csrf_protect, name='dispatch')
@method_decorator(login_required_json, name='dispatch')
class DeleteAccountView(View):
    """
    Gère la suppression du compte.
    """
    def post(self, request):
        try:
            user = request.user
            form = DeleteAccountForm(user, data=request.POST)
            if form.is_valid():
                logout(request)
                request.session.flush()  # Supprime les données de session
                user.delete()
                return JsonResponse({
                    'status': 'success', 
                    'message': _('Votre compte a été supprimé avec succès.')
                }, status=200)
            else:
                error_messages = " ".join([msg for messages in form.errors.values() for msg in messages])
                return JsonResponse({'status': 'error', 'message': error_messages}, status=400)
        except Exception as e:
            logger.exception("Erreur lors de la suppression du compte pour l'utilisateur %s: %s", request.user.username, str(e))
            return JsonResponse({'status': 'error', 'message': _("Une erreur interne est survenue.")}, status=500)
