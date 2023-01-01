from django.conf import settings

from .env import PUBNAME, SITE

GlobalContextData = dict(
    APPNAME=PUBNAME,
    SITE=SITE,
    CDN=settings.CDN_URL,
    ICON=f"{settings.CDN_URL}/graphics/self/icon.svg",
    ICON_DARK=f"{settings.CDN_URL}/graphics/self/icon-dark.svg",
    ICON_SHADOW=f"{settings.CDN_URL}/graphics/self/icon-shadow.svg",
    ICON_PNG=f"{settings.CDN_URL}/graphics/self/1024/icon.webp",
    ICON_DARK_PNG=f"{settings.CDN_URL}/graphics/self/1024/icon-dark.webp",
    ICON_SHADOW_PNG=f"{settings.CDN_URL}/graphics/self/1024/icon-shadow.webp",
    ICON_CIRCLE=f"{settings.CDN_URL}/graphics/self/icon-circle.svg",
    ICON_CIRCLE_DARK=f"{settings.CDN_URL}/graphics/self/icon-circle-dark.svg",
    BANNER=f"{settings.CDN_URL}/graphics/self/banner.svg",
    BANNER_PNG=f"{settings.CDN_URL}/graphics/self/2500x1000/banner-bg.webp",
)


def Global(request):
    data = dict(**GlobalContextData,
                alerts=[],
                SUBAPPS=dict(),
                SUBAPPSLIST=[],
                )

    return data
