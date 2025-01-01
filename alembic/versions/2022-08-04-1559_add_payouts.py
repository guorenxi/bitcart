"""Add payouts

Revision ID: be1f56ed9798
Revises: a050d461a6c1
Create Date: 2022-08-04 15:59:41.375425

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "be1f56ed9798"
down_revision: str | None = "a050d461a6c1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "payouts",
        sa.Column("id", sa.Text(), nullable=False),
        sa.Column("amount", sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column("destination", sa.Text(), nullable=True),
        sa.Column("currency", sa.Text(), nullable=True),
        sa.Column("status", sa.Text(), nullable=False),
        sa.Column("notification_url", sa.Text(), nullable=True),
        sa.Column("store_id", sa.Text(), nullable=True),
        sa.Column("wallet_id", sa.Text(), nullable=True),
        sa.Column("max_fee", sa.Numeric(precision=36, scale=18), nullable=True),
        sa.Column("tx_hash", sa.Text(), nullable=True),
        sa.Column("used_fee", sa.Numeric(precision=36, scale=18), nullable=True),
        sa.Column("user_id", sa.Text(), nullable=True),
        sa.Column("created", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["store_id"],
            ["stores.id"],
            name=op.f("payouts_store_id_stores_fkey"),
            ondelete="SET NULL",
            initially="DEFERRED",
            deferrable=True,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("payouts_user_id_users_fkey"), ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["wallet_id"],
            ["wallets.id"],
            name=op.f("payouts_wallet_id_wallets_fkey"),
            ondelete="SET NULL",
            initially="DEFERRED",
            deferrable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("payouts_pkey")),
    )
    op.create_index(op.f("payouts_id_idx"), "payouts", ["id"], unique=False)
    op.create_index(op.f("payouts_store_id_idx"), "payouts", ["store_id"], unique=False)
    op.create_index(op.f("payouts_wallet_id_idx"), "payouts", ["wallet_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("payouts_wallet_id_idx"), table_name="payouts")
    op.drop_index(op.f("payouts_store_id_idx"), table_name="payouts")
    op.drop_index(op.f("payouts_id_idx"), table_name="payouts")
    op.drop_table("payouts")
    # ### end Alembic commands ###
