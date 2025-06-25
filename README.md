[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Coverage Status](https://coveralls.io/repos/github/openaleph/ftm-transcribe/badge.svg?branch=main)](https://coveralls.io/github/openaleph/ftm-transcribe?branch=main)

# ftm-transcribe

Use [WhisperCPP](https://github.com/ggml-org/whisper.cpp) to transcribe audio and video files.

Follow the instructions in the WhisperCPP [README](https://github.com/ggml-org/whisper.cpp/blob/master/README.md) to build the binaries for your platform of choice.

Create a `.env` file in the root of this project and specify the following paths:

```
ftmtr_data_root=
ftmtr_whisper_executable=
ftmtr_whisper_model_root=
```

`ftmtr_data_root` corresponds to the directory where audio-only files and JSON files containing the transcription text will be stored temporarily.

`ftmtr_whisper_executable` is the full path to the `whisper-cli` executable.

`ftmtr_whisper_model_root` is the full path to the directory containing WhisperCPP models.

Optionally, the `.env` file can also contain the following values:

```
ftmtr_whisper_timeout=
ftmtr_whisper_model=
ftmtr_whisper_language=
```

## Usage

In order to run WhisperCPP on your device, install the library:

    poetry install

To run commands inside of the `.venv` created:

    $(poetry env activate)

To start an [openaleph-procrastinate worker](https://github.com/openaleph/openaleph-procrastinate) that can execute transcription tasks, start the worker from the command line:

    PROCRASTINATE_APP=ftm_transcribe.tasks.app procrastinate worker -q transcribe

To defer tasks from other places, use `transcribe` as queue name and `ftm_transcribe.tasks.transcribe` as the task identifier. These values can also be imported from [openaleph-procrastinate.settings](https://github.com/openaleph/openaleph-procrastinate/blob/main/openaleph_procrastinate/settings.py).

## License and Copyright

`ftm-transcribe`, (C) 2025 [Data and Research Center – DARC](https://dataresearchcenter.org)

`ftm-transcribe` is licensed under the AGPLv3 or later license.

see [NOTICE](./NOTICE) and [LICENSE](./LICENSE)
