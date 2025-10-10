from enum import Enum

# 模型配置字典
_MODEL_CONFIG = {
        "grok-3-fast": {
            "grok_model": ("grok-3", "MODEL_MODE_FAST"),
            "rate_limit_model": "grok-3",
            "cost": {"type": "low_cost", "multiplier": 1, "description": "计1次调用"},
            "requires_super": False,
            "display_name": "Grok 3 Fast",
            "description": "Fast and efficient Grok 3 model",
            "raw_model_path": "xai/grok-3",
            "default_temperature": 1.0,
            "default_max_output_tokens": 8192,
            "supported_max_output_tokens": 131072,
            "default_top_p": 0.95
        },
        "grok-4-fast": {
            "grok_model": ("grok-4-mini-thinking-tahoe", "MODEL_MODE_GROK_4_MINI_THINKING"),
            "rate_limit_model": "grok-4-mini-thinking-tahoe",
            "cost": {"type": "low_cost", "multiplier": 1, "description": "计1次调用"},
            "requires_super": False,
            "display_name": "Grok 4 Fast",
            "description": "Fast version of Grok 4 with mini thinking capabilities",
            "raw_model_path": "xai/grok-4-mini-thinking-tahoe",
            "default_temperature": 1.0,
            "default_max_output_tokens": 8192,
            "supported_max_output_tokens": 131072,
            "default_top_p": 0.95
        },
        "grok-4-fast-expert": {
            "grok_model": ("grok-4-mini-thinking-tahoe", "MODEL_MODE_EXPERT"),
            "rate_limit_model": "grok-4-mini-thinking-tahoe",
            "cost": {"type": "high_cost", "multiplier": 4, "description": "计4次调用"},
            "requires_super": False,
            "display_name": "Grok 4 Fast Expert",
            "description": "Expert mode of Grok 4 Fast with enhanced reasoning",
            "raw_model_path": "xai/grok-4-mini-thinking-tahoe",
            "default_temperature": 1.0,
            "default_max_output_tokens": 32768,
            "supported_max_output_tokens": 131072,
            "default_top_p": 0.95
        },
        "grok-4-expert": {
            "grok_model": ("grok-4", "MODEL_MODE_EXPERT"),
            "rate_limit_model": "grok-4",
            "cost": {"type": "high_cost", "multiplier": 4, "description": "计4次调用"},
            "requires_super": False,
            "display_name": "Grok 4 Expert",
            "description": "Full Grok 4 model with expert mode capabilities",
            "raw_model_path": "xai/grok-4",
            "default_temperature": 1.0,
            "default_max_output_tokens": 32768,
            "supported_max_output_tokens": 131072,
            "default_top_p": 0.95
        },
        "grok-4-heavy": {
            "grok_model": ("grok-4-heavy", "MODEL_MODE_HEAVY"),
            "rate_limit_model": "grok-4-heavy",
            "cost": {"type": "independent", "multiplier": 1, "description": "独立计费，只有Super用户可用"},
            "requires_super": True,
            "display_name": "Grok 4 Heavy",
            "description": "Most powerful Grok 4 model with heavy computational capabilities. Requires Super Token for access.",
            "raw_model_path": "xai/grok-4-heavy",
            "default_temperature": 1.0,
            "default_max_output_tokens": 65536,
            "supported_max_output_tokens": 131072,
            "default_top_p": 0.95
        }
    }

class TokenType(Enum):
    """Token类型枚举"""
    NORMAL = "ssoNormal"  # 普通用户Token
    SUPER = "ssoSuper"  # 超级用户Token


class Models(Enum):
    """支持的模型枚举"""
    GROK_3_FAST = "grok-3-fast"
    GROK_4_FAST = "grok-4-fast"
    GROK_4_FAST_EXPERT = "grok-4-fast-expert"
    GROK_4_EXPERT = "grok-4-expert"
    GROK_4_HEAVY = "grok-4-heavy"

    @classmethod
    def get_model_info(cls, model: str) -> dict:
        """获取模型的完整配置信息"""
        return _MODEL_CONFIG.get(model, {})

    @classmethod
    def is_valid_model(cls, model: str) -> bool:
        """检查模型是否有效"""
        return model in _MODEL_CONFIG
    
    @classmethod
    def to_grok(cls, model: str) -> tuple[str, str]:
        """转换为Grok内部模型名和模式类型"""
        config = _MODEL_CONFIG.get(model)
        if config:
            return config["grok_model"]
        return model, "MODEL_MODE_FAST"
    
    @classmethod
    def to_rate_limit(cls, model: str) -> str:
        """转换为速率限制接口模型名"""
        config = _MODEL_CONFIG.get(model)
        return config["rate_limit_model"] if config else model