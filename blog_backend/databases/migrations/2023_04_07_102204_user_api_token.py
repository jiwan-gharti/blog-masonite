"""UserApiToken Migration."""

from masoniteorm.migrations import Migration


class UserApiToken(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("api_token").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            pass
