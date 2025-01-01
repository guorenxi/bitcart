"""Add user_id to every model

Revision ID: c0fb4e374830
Revises: 43bab6d0af5b
Create Date: 2020-07-06 19:50:51.353165

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c0fb4e374830"
down_revision: str | None = "43bab6d0af5b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade_data() -> None:
    # stores
    op.execute(
        "update stores as stores_table set user_id=(select users.id from stores join"
        " walletsxstores on stores.id = walletsxstores.store_id join wallets on"
        " wallets.id = walletsxstores.wallet_id join users on users.id ="
        " wallets.user_id where stores.id = stores_table.id group by stores.id,"
        " users.id)"
    )
    # products
    op.execute(
        "update products as products_table set user_id=(select users.id from products"
        " join stores on stores.id = products.store_id join walletsxstores on stores.id"
        " = walletsxstores.store_id join wallets on wallets.id ="
        " walletsxstores.wallet_id join users on users.id = wallets.user_id where"
        " products.id = products_table.id group by products.id, users.id)"
    )
    # invoices
    op.execute(
        "update invoices as invoices_table set user_id=(select users.id from invoices"
        " join stores on stores.id = invoices.store_id join walletsxstores on stores.id"
        " = walletsxstores.store_id join wallets on wallets.id ="
        " walletsxstores.wallet_id join users on users.id = wallets.user_id where"
        " invoices.id = invoices_table.id group by invoices.id, users.id)"
    )


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("invoices", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("invoices_user_id_users_fkey"),
        "invoices",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.add_column("products", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("products_user_id_users_fkey"),
        "products",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.add_column("stores", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("stores_user_id_users_fkey"),
        "stores",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_index("ix_templates_name", table_name="templates")
    op.create_index(op.f("ix_templates_name"), "templates", ["name"], unique=True)
    op.drop_constraint("templates_name_key", "templates", type_="unique")
    # migrate data
    upgrade_data()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("templates_name_key", "templates", ["name"])
    op.drop_index(op.f("ix_templates_name"), table_name="templates")
    op.create_index("ix_templates_name", "templates", ["name"], unique=False)
    op.drop_constraint(None, "stores", type_="foreignkey")  # type: ignore
    op.drop_column("stores", "user_id")
    op.drop_constraint(None, "products", type_="foreignkey")  # type: ignore
    op.drop_column("products", "user_id")
    op.drop_constraint(None, "invoices", type_="foreignkey")  # type: ignore
    op.drop_column("invoices", "user_id")
    # ### end Alembic commands ###
