"""004_create_applications_table

Revision ID: 0c8d034ac3d6
Revises: 954cb22cc24c
Create Date: 2026-04-01 16:54:05.265392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c8d034ac3d6'
down_revision: Union[str, Sequence[str], None] = '954cb22cc24c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('application_date', sa.Date(), nullable=True),
    sa.Column('job_link', sa.String(), nullable=True),
    sa.Column('job_description', sa.Text(), nullable=True),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),

    sa.Column('created_by', sa.String(length=50), server_default='SYSTEM', nullable=False),
    sa.Column('modified_by', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),

    sa.ForeignKeyConstraint(['resume_id'], ['resumes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_index('ix_applications_user_id', 'applications', ['user_id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_applications_user_id', table_name='applications')
    op.drop_table('applications')