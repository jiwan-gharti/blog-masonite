"""UserApiToken Migration."""

from masoniteorm.migrations import Migration


class UserApiToken(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("user") as table:
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("user") as table:
            pass
