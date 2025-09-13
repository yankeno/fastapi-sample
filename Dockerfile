FROM python:3.9

WORKDIR /app

# uvをインストール
RUN pip install uv

# uvで仮想環境を作成
RUN uv venv

# 仮想環境をアクティベート
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml ./
COPY uv.lock ./

# uvで依存関係をインストール
RUN uv sync --frozen

COPY . .

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
