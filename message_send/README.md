# Teams webhook

- 서비스 장애시 알림을 받기 위해 시작
- 메신저로 팀즈를 사용하여 팀내 비공개 채널을 개설
- 채널 -> 앱 에서 Incoming Webhook를 추가
- [참고 블로그](https://jh-bk.tistory.com/39)

### Retirement of Office 365 connectors within Microsoft Teams

- [ms dev blog](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/)

# Teams Workflows

- workflows 기능을 이용해 기존 알림을 받고자 함
- 기능이 제한적임
- 구성하는데 참고 자료가 적고, 불친절하며 버그도 존재
- 결정적으로 형식이 고정되어 받아야 하는 메시지가 잘림(방법을 못찾음)

### 시행착오

- 팀의 채널에서 워크플로우를 타고 들어가면 탬플릿이 있는데 "웹후크 요청이 수신되면 채널에 게시"를 사용하고자 함
- flow 생성이 되었지만 팀 정보가 비어있음 -> 채널에서 워크플로우를 들어가지말고 사이드 바에 점 세개를 눌러 워크플로우를 들어가면 팀 정보를 입력할 수 있음
- 생성된 플로우에서 채널이 비공개면 flow-bot을 사용할 수 없음 -> 유저로 해야 사용가능

# SMTP

- outlook으로 알림을 받고 정해진 title은 규칙을 정해 원하는 폴더에 적재할 수 있음
- 주의: 파일명을 email.py로 하지 말 것.

# SLACK

- 만약 사내 메신저로 slack을 사용했다면 slack으로 구성 했을 것임
- 참고 자료 다수, 구성 쉬움
