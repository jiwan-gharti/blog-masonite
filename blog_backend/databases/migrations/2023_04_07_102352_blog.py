"""Blog Migration."""

from masoniteorm.migrations import Migration
from masoniteorm.scopes import SoftDeletesMixin


class Blog(Migration,SoftDeletesMixin):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id").primary()
            table.string("title")
            table.string("content")
            table.string('image').nullable()
            table.integer("user_id")
            table.foreign('user_id').references('id').on("users").on_delete('set null')
            
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")
