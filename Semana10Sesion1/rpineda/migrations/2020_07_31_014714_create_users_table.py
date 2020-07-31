from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.string('name').unique()
            table.string('email').unique()
            table.increments('id')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')