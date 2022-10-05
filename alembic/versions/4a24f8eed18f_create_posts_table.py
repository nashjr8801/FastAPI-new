"""create posts table

Revision ID: 4a24f8eed18f
Revises: 
Create Date: 2022-10-05 19:41:07.876392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a24f8eed18f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))    
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
