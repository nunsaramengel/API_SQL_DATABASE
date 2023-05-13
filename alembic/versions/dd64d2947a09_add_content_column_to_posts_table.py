"""add content column to posts table

Revision ID: dd64d2947a09
Revises: 8f79744f94a2
Create Date: 2023-05-13 08:12:17.273532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd64d2947a09'
down_revision = '8f79744f94a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
