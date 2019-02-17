from rest_framework.routers import SimpleRouter

from snipetto.snippets.views import SnippetViewSet, TagViewSet

router = SimpleRouter()
router.register('tags', TagViewSet, base_name='tags')
router.register('snippets', SnippetViewSet, base_name='snippets')

urlpatterns = router.urls
