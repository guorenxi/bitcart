"""Full partial payments support

Revision ID: 2d6563c7943d
Revises: 3801b9cf3278
Create Date: 2023-01-04 16:33:12.956781

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2d6563c7943d"
down_revision: str | None = "3801b9cf3278"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("invoices", sa.Column("sent_amount", sa.Numeric(precision=36, scale=18), nullable=True, server_default="0"))
    op.alter_column("invoices", "sent_amount", server_default=None)
    op.add_column("invoices", sa.Column("exception_status", sa.Text(), nullable=True, server_default="none"))
    op.alter_column("invoices", "exception_status", server_default=None)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("invoices", "exception_status")
    op.drop_column("invoices", "sent_amount")
    # ### end Alembic commands ###
