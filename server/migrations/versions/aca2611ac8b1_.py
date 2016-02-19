"""empty message

Revision ID: aca2611ac8b1
Revises: 0289ce4fa360
Create Date: 2016-02-18 20:53:21.254104

"""

# revision identifiers, used by Alembic.
revision = 'aca2611ac8b1'
down_revision = '0289ce4fa360'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('photo', sa.String(length=100), nullable=True))
    op.drop_constraint('person_email_key', 'person', type_='unique')
    op.drop_column('person', 'email')
    op.drop_column('person', 'website')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('website', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('person', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_unique_constraint('person_email_key', 'person', ['email'])
    op.drop_column('person', 'photo')
    ### end Alembic commands ###