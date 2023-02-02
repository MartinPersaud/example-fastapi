"""add content column to posts table

Revision ID: cd092ae8ed0b
Revises: ac20ec321ed3
Create Date: 2023-02-02 12:16:44.363293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd092ae8ed0b'
down_revision = 'ac20ec321ed3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
