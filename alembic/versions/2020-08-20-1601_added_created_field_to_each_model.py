"""Added created field to each model

Revision ID: d47757e34b68
Revises: a2891d77e92b
Create Date: 2020-08-20 16:01:46.255237

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d47757e34b68"
down_revision: str | None = "a2891d77e92b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def add_creation_date(table):
    op.add_column(
        table,
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.clock_timestamp(),  # to differ in context of current transaction
        ),
    )
    op.alter_column(table, "created", server_default=None)


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    add_creation_date("discounts")
    op.alter_column(
        "invoices",
        column_name="date",
        new_column_name="created",
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=None,
    )
    add_creation_date("notifications")
    op.alter_column(
        "products",
        column_name="date",
        new_column_name="created",
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=None,
    )
    add_creation_date("settings")
    add_creation_date("stores")
    add_creation_date("templates")
    add_creation_date("tokens")
    add_creation_date("users")
    add_creation_date("wallets")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("wallets", "created")
    op.drop_column("users", "created")
    op.drop_column("tokens", "created")
    op.drop_column("templates", "created")
    op.drop_column("stores", "created")
    op.drop_column("settings", "created")
    op.alter_column(
        "invoices",
        column_name="created",
        new_column_name="date",
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=None,
    )
    op.drop_column("notifications", "created")
    op.alter_column(
        "products",
        column_name="created",
        new_column_name="date",
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=None,
    )
    op.drop_column("discounts", "created")
    # ### end Alembic commands ###
