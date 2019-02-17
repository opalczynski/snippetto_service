from rest_framework.routers import SimpleRouter

from snipetto.snippets.views import TagViewSet, SnippetViewSet

router = SimpleRouter()
router.register('tags', TagViewSet, base_name='tags')
router.register('snippets', SnippetViewSet, base_name='snippets')

urlpatterns = router.urls
