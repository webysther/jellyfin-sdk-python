# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from jellyfin.generated.api_10_11.api.activity_log_api import ActivityLogApi
    from jellyfin.generated.api_10_11.api.api_key_api import ApiKeyApi
    from jellyfin.generated.api_10_11.api.artists_api import ArtistsApi
    from jellyfin.generated.api_10_11.api.audio_api import AudioApi
    from jellyfin.generated.api_10_11.api.backup_api import BackupApi
    from jellyfin.generated.api_10_11.api.branding_api import BrandingApi
    from jellyfin.generated.api_10_11.api.channels_api import ChannelsApi
    from jellyfin.generated.api_10_11.api.client_log_api import ClientLogApi
    from jellyfin.generated.api_10_11.api.collection_api import CollectionApi
    from jellyfin.generated.api_10_11.api.configuration_api import ConfigurationApi
    from jellyfin.generated.api_10_11.api.dashboard_api import DashboardApi
    from jellyfin.generated.api_10_11.api.devices_api import DevicesApi
    from jellyfin.generated.api_10_11.api.display_preferences_api import DisplayPreferencesApi
    from jellyfin.generated.api_10_11.api.dynamic_hls_api import DynamicHlsApi
    from jellyfin.generated.api_10_11.api.environment_api import EnvironmentApi
    from jellyfin.generated.api_10_11.api.filter_api import FilterApi
    from jellyfin.generated.api_10_11.api.genres_api import GenresApi
    from jellyfin.generated.api_10_11.api.hls_segment_api import HlsSegmentApi
    from jellyfin.generated.api_10_11.api.image_api import ImageApi
    from jellyfin.generated.api_10_11.api.instant_mix_api import InstantMixApi
    from jellyfin.generated.api_10_11.api.item_lookup_api import ItemLookupApi
    from jellyfin.generated.api_10_11.api.item_refresh_api import ItemRefreshApi
    from jellyfin.generated.api_10_11.api.item_update_api import ItemUpdateApi
    from jellyfin.generated.api_10_11.api.items_api import ItemsApi
    from jellyfin.generated.api_10_11.api.library_api import LibraryApi
    from jellyfin.generated.api_10_11.api.library_structure_api import LibraryStructureApi
    from jellyfin.generated.api_10_11.api.live_tv_api import LiveTvApi
    from jellyfin.generated.api_10_11.api.localization_api import LocalizationApi
    from jellyfin.generated.api_10_11.api.lyrics_api import LyricsApi
    from jellyfin.generated.api_10_11.api.media_info_api import MediaInfoApi
    from jellyfin.generated.api_10_11.api.media_segments_api import MediaSegmentsApi
    from jellyfin.generated.api_10_11.api.movies_api import MoviesApi
    from jellyfin.generated.api_10_11.api.music_genres_api import MusicGenresApi
    from jellyfin.generated.api_10_11.api.package_api import PackageApi
    from jellyfin.generated.api_10_11.api.persons_api import PersonsApi
    from jellyfin.generated.api_10_11.api.playlists_api import PlaylistsApi
    from jellyfin.generated.api_10_11.api.playstate_api import PlaystateApi
    from jellyfin.generated.api_10_11.api.plugins_api import PluginsApi
    from jellyfin.generated.api_10_11.api.quick_connect_api import QuickConnectApi
    from jellyfin.generated.api_10_11.api.remote_image_api import RemoteImageApi
    from jellyfin.generated.api_10_11.api.scheduled_tasks_api import ScheduledTasksApi
    from jellyfin.generated.api_10_11.api.search_api import SearchApi
    from jellyfin.generated.api_10_11.api.session_api import SessionApi
    from jellyfin.generated.api_10_11.api.startup_api import StartupApi
    from jellyfin.generated.api_10_11.api.studios_api import StudiosApi
    from jellyfin.generated.api_10_11.api.subtitle_api import SubtitleApi
    from jellyfin.generated.api_10_11.api.suggestions_api import SuggestionsApi
    from jellyfin.generated.api_10_11.api.sync_play_api import SyncPlayApi
    from jellyfin.generated.api_10_11.api.system_api import SystemApi
    from jellyfin.generated.api_10_11.api.time_sync_api import TimeSyncApi
    from jellyfin.generated.api_10_11.api.tmdb_api import TmdbApi
    from jellyfin.generated.api_10_11.api.trailers_api import TrailersApi
    from jellyfin.generated.api_10_11.api.trickplay_api import TrickplayApi
    from jellyfin.generated.api_10_11.api.tv_shows_api import TvShowsApi
    from jellyfin.generated.api_10_11.api.universal_audio_api import UniversalAudioApi
    from jellyfin.generated.api_10_11.api.user_api import UserApi
    from jellyfin.generated.api_10_11.api.user_library_api import UserLibraryApi
    from jellyfin.generated.api_10_11.api.user_views_api import UserViewsApi
    from jellyfin.generated.api_10_11.api.video_attachments_api import VideoAttachmentsApi
    from jellyfin.generated.api_10_11.api.videos_api import VideosApi
    from jellyfin.generated.api_10_11.api.years_api import YearsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from jellyfin.generated.api_10_11.api.activity_log_api import ActivityLogApi
from jellyfin.generated.api_10_11.api.api_key_api import ApiKeyApi
from jellyfin.generated.api_10_11.api.artists_api import ArtistsApi
from jellyfin.generated.api_10_11.api.audio_api import AudioApi
from jellyfin.generated.api_10_11.api.backup_api import BackupApi
from jellyfin.generated.api_10_11.api.branding_api import BrandingApi
from jellyfin.generated.api_10_11.api.channels_api import ChannelsApi
from jellyfin.generated.api_10_11.api.client_log_api import ClientLogApi
from jellyfin.generated.api_10_11.api.collection_api import CollectionApi
from jellyfin.generated.api_10_11.api.configuration_api import ConfigurationApi
from jellyfin.generated.api_10_11.api.dashboard_api import DashboardApi
from jellyfin.generated.api_10_11.api.devices_api import DevicesApi
from jellyfin.generated.api_10_11.api.display_preferences_api import DisplayPreferencesApi
from jellyfin.generated.api_10_11.api.dynamic_hls_api import DynamicHlsApi
from jellyfin.generated.api_10_11.api.environment_api import EnvironmentApi
from jellyfin.generated.api_10_11.api.filter_api import FilterApi
from jellyfin.generated.api_10_11.api.genres_api import GenresApi
from jellyfin.generated.api_10_11.api.hls_segment_api import HlsSegmentApi
from jellyfin.generated.api_10_11.api.image_api import ImageApi
from jellyfin.generated.api_10_11.api.instant_mix_api import InstantMixApi
from jellyfin.generated.api_10_11.api.item_lookup_api import ItemLookupApi
from jellyfin.generated.api_10_11.api.item_refresh_api import ItemRefreshApi
from jellyfin.generated.api_10_11.api.item_update_api import ItemUpdateApi
from jellyfin.generated.api_10_11.api.items_api import ItemsApi
from jellyfin.generated.api_10_11.api.library_api import LibraryApi
from jellyfin.generated.api_10_11.api.library_structure_api import LibraryStructureApi
from jellyfin.generated.api_10_11.api.live_tv_api import LiveTvApi
from jellyfin.generated.api_10_11.api.localization_api import LocalizationApi
from jellyfin.generated.api_10_11.api.lyrics_api import LyricsApi
from jellyfin.generated.api_10_11.api.media_info_api import MediaInfoApi
from jellyfin.generated.api_10_11.api.media_segments_api import MediaSegmentsApi
from jellyfin.generated.api_10_11.api.movies_api import MoviesApi
from jellyfin.generated.api_10_11.api.music_genres_api import MusicGenresApi
from jellyfin.generated.api_10_11.api.package_api import PackageApi
from jellyfin.generated.api_10_11.api.persons_api import PersonsApi
from jellyfin.generated.api_10_11.api.playlists_api import PlaylistsApi
from jellyfin.generated.api_10_11.api.playstate_api import PlaystateApi
from jellyfin.generated.api_10_11.api.plugins_api import PluginsApi
from jellyfin.generated.api_10_11.api.quick_connect_api import QuickConnectApi
from jellyfin.generated.api_10_11.api.remote_image_api import RemoteImageApi
from jellyfin.generated.api_10_11.api.scheduled_tasks_api import ScheduledTasksApi
from jellyfin.generated.api_10_11.api.search_api import SearchApi
from jellyfin.generated.api_10_11.api.session_api import SessionApi
from jellyfin.generated.api_10_11.api.startup_api import StartupApi
from jellyfin.generated.api_10_11.api.studios_api import StudiosApi
from jellyfin.generated.api_10_11.api.subtitle_api import SubtitleApi
from jellyfin.generated.api_10_11.api.suggestions_api import SuggestionsApi
from jellyfin.generated.api_10_11.api.sync_play_api import SyncPlayApi
from jellyfin.generated.api_10_11.api.system_api import SystemApi
from jellyfin.generated.api_10_11.api.time_sync_api import TimeSyncApi
from jellyfin.generated.api_10_11.api.tmdb_api import TmdbApi
from jellyfin.generated.api_10_11.api.trailers_api import TrailersApi
from jellyfin.generated.api_10_11.api.trickplay_api import TrickplayApi
from jellyfin.generated.api_10_11.api.tv_shows_api import TvShowsApi
from jellyfin.generated.api_10_11.api.universal_audio_api import UniversalAudioApi
from jellyfin.generated.api_10_11.api.user_api import UserApi
from jellyfin.generated.api_10_11.api.user_library_api import UserLibraryApi
from jellyfin.generated.api_10_11.api.user_views_api import UserViewsApi
from jellyfin.generated.api_10_11.api.video_attachments_api import VideoAttachmentsApi
from jellyfin.generated.api_10_11.api.videos_api import VideosApi
from jellyfin.generated.api_10_11.api.years_api import YearsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
