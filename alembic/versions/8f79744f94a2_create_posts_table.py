"""Create posts table

Revision ID: 8f79744f94a2
Revises: 
Create Date: 2023-05-13 07:56:19.233440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f79744f94a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
