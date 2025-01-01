"""Support multiple captcha

Revision ID: 91e2cdaa49b5
Revises: 818bb0f07e9b
Create Date: 2024-03-19 16:02:19.347055

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "91e2cdaa49b5"
down_revision: str | None = "818bb0f07e9b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        """
        UPDATE settings
        SET value = jsonb_set(
            value::jsonb - '{enable_captcha}',
            '{captcha_type}'::text[],
            CASE WHEN value::jsonb->>'enable_captcha' = 'true' THEN '"hcaptcha"'::jsonb ELSE '"none"'::jsonb END
        )
        WHERE name = 'policy'
    """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        """
        UPDATE settings
        SET value = jsonb_set(
            value::jsonb - '{captcha_type}',
            '{enable_captcha}'::text[],
            CASE WHEN value::jsonb->>'captcha_type' = 'hcaptcha' THEN 'true'::jsonb ELSE 'false'::jsonb END
        )
        WHERE name = 'policy'
    """
    )
    # ### end Alembic commands ###
