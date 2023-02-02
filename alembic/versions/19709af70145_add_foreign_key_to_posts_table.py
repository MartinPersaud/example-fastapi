"""add foreign-key to posts table

Revision ID: 19709af70145
Revises: 0d3359573797
Create Date: 2023-02-02 14:28:43.756694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19709af70145'
down_revision = '0d3359573797'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", 
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
