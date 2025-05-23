from .approval import approval_view  # noqa: F401
from .auth import login_view, logout_view, register_view  # noqa: F401
from .main import index_view  # noqa: F401
from .request import (  # noqa: F401
    request_create_view,
    request_delete_view,
    request_detail_view,
    request_edit_view,
)
