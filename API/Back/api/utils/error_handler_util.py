class ErrorHandler(Exception):
    """Classe de base pour les erreurs personnalisées."""

    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

# Auth_view
class UserNotFoundError(ErrorHandler):
    """Erreur levée lorsqu'un utilisateur n'est pas trouvé."""

    def __init__(self, message="Utilisateur non trouvé"):
        super().__init__(message, status_code=404)

class UserAlreadyExistsError(ErrorHandler):
    """Erreur levée lorsqu'un utilisateur existe déjà."""

    def __init__(self, message="L'utilisateur existe déjà"):
        super().__init__(message, status_code=400)

class InvalidCredentialsError(ErrorHandler):
    """Erreur levée lorsque les identifiants sont invalides."""

    def __init__(self, message="Identifiants invalides"):
        super().__init__(message, status_code=401)

class EmailAndPasswordRequiredError(ErrorHandler):
    """Erreur levée lorsque l'email et password sont manquants."""

    def __init__(self, message="L'adresse e-mail et le mot de passe sont requis"):
        super().__init__(message, status_code=400)

#decorator_util
class InvalidTokenOrRequiredError(ErrorHandler):
    """Erreur lévee lorsque le token est manquant ou invalide."""

    def __init__(self, message="Token manquant ou invalide dans les en-têtes de la requête"):
        super().__init__(message, status_code=401)

class UnauthorizedError(ErrorHandler):
    """Erreur levée lorsque l'utilisateur n'a pas les autorisations nécessaires."""

    def __init__(self, message="Vous n'avez pas les autorisations nécessaires pour accéder à cette ressource"):
        super().__init__(message, status_code=403)

class UserIdMismatchError(ErrorHandler):
    """Erreur levée lorsque l'identifiant de l'utilisateur ne correspond pas."""
    
    def __init__(self, message="Vous n'êtes pas autorisé à effectuer cette opération"):
        super().__init__(message, status_code=403)