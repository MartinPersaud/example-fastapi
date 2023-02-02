"""create posts table

Revision ID: ac20ec321ed3
Revises: 
Create Date: 2023-02-02 11:48:51.653226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac20ec321ed3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True,),
                    sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_table('posts')
    
    pass
