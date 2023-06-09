"""Add last few columns to posts table

Revision ID: 28196a9af202
Revises: b09a292e41f2
Create Date: 2023-05-13 08:44:33.520368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28196a9af202'
down_revision = 'b09a292e41f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),)
    pass


def downgrade() -> None:
    op.drop_column('posts', "published")
    op.drop_column('posts', "created_at")
    pass
