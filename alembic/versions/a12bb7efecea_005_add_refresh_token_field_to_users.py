"""005_add_refresh_token_field_to_users

Revision ID: a12bb7efecea
Revises: 0c8d034ac3d6
Create Date: 2026-04-03 16:57:01.705529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a12bb7efecea'
down_revision: Union[str, Sequence[str], None] = '0c8d034ac3d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('refresh_token', sa.String(), nullable=True))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'refresh_token')