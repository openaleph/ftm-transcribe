from openaleph_procrastinate.app import make_app
from openaleph_procrastinate.model import DatasetJob
from openaleph_procrastinate.tasks import task

from ftm_transcribe.settings import Settings

settings = Settings()
app = make_app(__loader__.name)

ORIGIN = "ftm-transcribe"


@task(app=app)
def transcribe(job: DatasetJob) -> DatasetJob:
    print("AAAAAA")
    # for entity_file_reference in job.get_file_references():
    #     local_path = entity_file_reference.get_localpath()
    #     print(local_path)
    # for entity, handler in job.get_file_references():
    #     with handler.get_localpath() as path:
    #         subprocess.run(f"some-program -f {path}")
    return job
