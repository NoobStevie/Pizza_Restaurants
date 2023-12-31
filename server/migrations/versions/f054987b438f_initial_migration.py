"""Initial migration

Revision ID: f054987b438f
Revises: 
Create Date: 2023-10-04 08:59:19.749002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f054987b438f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], name=op.f('fk_restaurant_pizzas_pizza_id_pizzas')),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], name=op.f('fk_restaurant_pizzas_restaurant_id_restaurants')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredients', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=True)
        batch_op.drop_column('price')

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.REAL(), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('ingredients')

    op.drop_table('restaurant_pizzas')
    # ### end Alembic commands ###
