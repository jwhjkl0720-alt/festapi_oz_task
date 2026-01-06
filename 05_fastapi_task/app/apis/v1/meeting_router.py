from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND


from app.dtos.get_meeting_response import GetMeetingResponse
from app.services.meeting_service_edgedb import (
    service_create_meeting_edgedb,
    service_get_meeting_edgedb,
)


@edgedb_router.get(
    "/{meeting_url_code}",
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeetingResponse:
    meeting = await service_get_meeting_edgedb(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return GetMeetingResponse(url_code=meeting.url_code)

...
@mysql_router.get(
    "/{meeting_url_code}",  # path variable
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    meeting = await service_get_meeting_mysql(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return GetMeetingResponse(url_code=meeting.url_code)
