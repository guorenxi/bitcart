"""Add id to payment methods

Revision ID: dfa080636f10
Revises: 5bf0a0845afb
Create Date: 2021-01-19 22:55:25.013299

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence, DropSequence
from sqlalchemy.schema import Sequence as SQLSequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "dfa080636f10"
down_revision: str | None = "5bf0a0845afb"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(CreateSequence(SQLSequence("paymentmethods_id_seq")))  # type: ignore # TODO: when merging in one file, investigate
    op.add_column(
        "paymentmethods",
        sa.Column("id", sa.Integer(), nullable=False, server_default=sa.text("nextval('paymentmethods_id_seq'::regclass)")),
    )
    op.create_primary_key("paymentmethods_pkey", "paymentmethods", ["id"])
    op.create_index(op.f("paymentmethods_id_idx"), "paymentmethods", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("paymentmethods_pkey", table_name="paymentmethods")
    op.drop_index(op.f("paymentmethods_id_idx"), table_name="paymentmethods")
    op.drop_column("paymentmethods", "id")
    op.execute(DropSequence(SQLSequence("paymentmethods_id_seq")))  # type: ignore
    # ### end Alembic commands ###
