"""003_create_resumes_table

Revision ID: 954cb22cc24c
Revises: 948390647479
Create Date: 2026-04-01 16:46:15.359083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '954cb22cc24c'
down_revision: Union[str, Sequence[str], None] = '948390647479'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('resumes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('version_label', sa.String(), nullable=True),
    sa.Column('uploaded_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),

    sa.Column('created_by', sa.String(length=50), server_default='SYSTEM', nullable=False),
    sa.Column('modified_by', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),

    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_index('ix_resumes_user_id', 'resumes', ['user_id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_resumes_user_id', table_name='resumes')
    op.drop_table('resumes')