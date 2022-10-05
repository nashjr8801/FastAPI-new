"""add content column to posts table

Revision ID: c246aa758fc9
Revises: 4a24f8eed18f
Create Date: 2022-10-05 19:51:19.121951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c246aa758fc9'
down_revision = '4a24f8eed18f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
        

    
