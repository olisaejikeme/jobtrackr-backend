"""002_create_users_table

Revision ID: 948390647479
Revises: b98d43ea21a0
Create Date: 2026-04-01 16:38:56.999338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '948390647479'
down_revision: Union[str, Sequence[str], None] = 'b98d43ea21a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),

    sa.Column('created_by', sa.String(length=50), server_default='SYSTEM', nullable=False),
    sa.Column('modified_by', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),

    sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')