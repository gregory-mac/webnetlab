"""initial

Revision ID: 03ba2956af0e
Revises: 
Create Date: 2022-08-15 00:04:16.184981

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import Integer, String, Boolean

# revision identifiers, used by Alembic.
revision = '03ba2956af0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", Integer, primary_key=True),
        sa.Column("login", String(30), nullable=False, unique=True),
        sa.Column("email", String(50), nullable=False, unique=True),
        sa.Column("is_admin", Boolean, nullable=False, unique=False, default=False),
    )


def downgrade() -> None:
    op.drop_table("users")
