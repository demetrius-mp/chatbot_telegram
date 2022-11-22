from typing import Any, Optional, Tuple

import torch
import transformers
from sklearn.preprocessing import LabelEncoder


class LIABertClassifier(torch.nn.Module):
    bert: Any

    def __init__(self, model, num_labels, bert_attr="bert"):
        super(LIABertClassifier, self).__init__()
        try:
            self.bert = model.bert
        except AttributeError:
            self.bert = model.roberta
        self.config = model.config
        self.num_labels = num_labels
        self.cls = torch.nn.Linear(self.config.hidden_size, num_labels)

    def forward(
        self,
        input_ids: Optional[torch.Tensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor]:

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )

        sequence_output = outputs[0][:, 0, :]
        prediction = self.cls(sequence_output)
        return prediction


def use_model(model_name: str):
    model_base = transformers.AutoModelForPreTraining.from_pretrained(model_name)
    model = LIABertClassifier(model=model_base, num_labels=3)

    return model


best_model_checkpoint = torch.load("best_model.pth", map_location=torch.device("cpu"))


best_model = use_model(best_model_checkpoint["model_name"])
best_model.load_state_dict(best_model_checkpoint["model"])
le = LabelEncoder()
le.classes_ = best_model_checkpoint["encoder_classes"]
tokenizer = transformers.AutoTokenizer.from_pretrained(
    best_model_checkpoint["model_name"], do_lower_case=False
)

intencoes = ["fazer pedido", "fechar conta", "ver cardápio"]


def make_prediction(text):
    token = tokenizer(text, return_tensors="pt")
    pred = best_model(**token)

    return le.inverse_transform(pred.argmax(dim=-1))[0]  # type: ignore
