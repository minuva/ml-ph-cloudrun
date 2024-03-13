import logging
import os

from typing import Dict, Union
from fastapi import APIRouter
from .schema import TaskInput
from src.emotion import get_task_user_agent_emotion
from src.flow import get_task_flow_labels
from src.toxic import get_task_user_agent_toxic, CustomDetoxify
from src.model import OnnxTransformer
from tokenizers import Tokenizer
from src.model import OnnxTransformer
from tokenizers import Tokenizer


device = "cpu"

logger = logging.getLogger(__name__)
router = APIRouter()

# go emotion cfg
emotion_model_name = "MiniLMv2-goemotions-v2-onnx"
tokenizer = Tokenizer.from_pretrained("minuva/MiniLMv2-goemotions-v2-onnx")
tokenizer.enable_truncation(max_length=256)
emotion_model = OnnxTransformer(
    emotion_model_name,
)

# Toxic cfg
toxic_model_name = "MiniLMv2-toxic-jigsaw-lite-onnx"
toxic_model = CustomDetoxify(toxic_model_name)


# Flow cfg
agent_flow_model_name = "MiniLMv2-agentflow-v2-onnx"
user_flow_model_name = "MiniLMv2-userflow-v2-onnx"

agent_flow_model = OnnxTransformer(agent_flow_model_name)
user_flow_model = OnnxTransformer(user_flow_model_name)

flow_tokenizer_user = Tokenizer.from_file(
    os.path.join(user_flow_model_name, "tokenizer.json")
)
flow_tokenizer_user.enable_padding(pad_token="<pad>", pad_id=1)
flow_tokenizer_user.enable_truncation(max_length=256)


flow_tokenizer_agent = Tokenizer.from_file(
    os.path.join(agent_flow_model_name, "tokenizer.json")
)
flow_tokenizer_agent.enable_padding(pad_token="<pad>", pad_id=1)
flow_tokenizer_agent.enable_truncation(max_length=256)

@router.get("/")
async def root():
    return {"message": "minuva API"}




@router.post("/conversation_emotions_plugin", response_model=Dict[str, str])
async def task_emotions(
    request: TaskInput
):
    return get_task_user_agent_emotion(request.llm_input, request.llm_output, emotion_model, tokenizer)


@router.post("/conversation_toxicity_plugin", response_model=Dict[str, Union[str, int]])
async def task_toxic(
    request: TaskInput
):
    return get_task_user_agent_toxic(request.llm_input, request.llm_output, toxic_model)


@router.post("/conversation_flow_plugin", response_model=Dict[str, str])
async def task_flow(
    request: TaskInput
):
    user_flow = get_task_flow_labels(request.llm_input, user_flow_model, flow_tokenizer_user)
    agent_flow = get_task_flow_labels(request.llm_output, agent_flow_model, flow_tokenizer_agent)
    return {"user_flow": user_flow, "agent_flow": agent_flow}
