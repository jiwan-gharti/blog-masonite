"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create(
            title="title 2",
            content="content of title 23",
            image = "first.png",
            user_id = 2
        )
        
