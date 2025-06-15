from usecases.user import UserUsecase


def get_user_usecase() -> UserUsecase:
    """Get the user usecase.

    Returns:
        The user usecase.

    """
    return UserUsecase()
