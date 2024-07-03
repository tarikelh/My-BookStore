from django.http import JsonResponse
from django.views import View
import json
from ..models.User import User
from ..dao.user_dao import UserDAO
from ..utils.jwt_util import JWT
from ..utils.error_handler_util import InvalidCredentialsError, EmailAndPasswordRequiredError, UserAlreadyExistsError

class LoginView(View):
    """View class for user login."""

    def post(self, request):
        """Handle POST requests for user login."""
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            user = UserDAO.get_user_by_email(email)
            if user and user.check_password(password):
                data = {
                    'user_id': user.id,
                    'email': user.email,
                    'role': user.role
                }
                token = JWT.generate_jwt_token(data)
                return JsonResponse({'success': True, 'token': token})
            else:
                raise InvalidCredentialsError()
            
        except InvalidCredentialsError as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=e.status_code)
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': "L'utilisateur n'existe pas"}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

class RegisterView(View):
    """View class for user registration."""
    
    def post(self, request):
        """Handle POST requests for user registration."""
        try:
            data = json.loads(request.body)
            password = data.get('password')
            email = data.get('email')
            
            if not email or not password:
                raise EmailAndPasswordRequiredError()

            if UserDAO.get_user_by_email(email):
                raise UserAlreadyExistsError()
  
            data['role'] = 'user'
            
            UserDAO.save_or_update(User, data)
            return JsonResponse({'success': True, 'message': 'Utilisateur enregistré avec succès'})
        except EmailAndPasswordRequiredError as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=e.status_code)
        except UserAlreadyExistsError as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=e.status_code)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
