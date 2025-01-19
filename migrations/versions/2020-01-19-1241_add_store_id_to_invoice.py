"""Add store_id to invoice

Revision ID: 23db42f6e0e7
Revises: f5070830387b
Create Date: 2020-01-19 12:41:26.690465

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "23db42f6e0e7"
down_revision: str | None = "f5070830387b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("invoices", sa.Column("order_id", sa.Text(), nullable=True))
    op.add_column("invoices", sa.Column("store_id", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_invoices_store_id"), "invoices", ["store_id"], unique=False)
    op.create_foreign_key(
        None,
        "invoices",
        "stores",
        ["store_id"],
        ["id"],
        ondelete="SET NULL",
        initially="DEFERRED",
        deferrable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "invoices", type_="foreignkey")  # type: ignore
    op.drop_index(op.f("ix_invoices_store_id"), table_name="invoices")
    op.drop_column("invoices", "store_id")
    op.drop_column("invoices", "order_id")
    # ### end Alembic commands ###