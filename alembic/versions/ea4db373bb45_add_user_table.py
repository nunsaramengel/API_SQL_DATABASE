"""add user  table

Revision ID: ea4db373bb45
Revises: dd64d2947a09
Create Date: 2023-05-13 08:23:53.540066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea4db373bb45'
down_revision = 'dd64d2947a09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table("users")
    pass
