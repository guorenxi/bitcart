"""Store invoice expiration

Revision ID: a2891d77e92b
Revises: 65986008ad26
Create Date: 2020-08-19 17:23:37.273115

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a2891d77e92b"
down_revision: str | None = "65986008ad26"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("stores", sa.Column("expiration", sa.Integer(), nullable=True, server_default="15"))
    op.add_column("invoices", sa.Column("expiration", sa.Integer(), nullable=True, server_default="15"))
    op.alter_column("stores", "expiration", server_default=None)
    op.alter_column("invoices", "expiration", server_default=None)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("stores", "expiration")
    op.drop_column("invoices", "expiration")
    # ### end Alembic commands ###
