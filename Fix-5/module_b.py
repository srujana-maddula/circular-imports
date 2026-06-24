from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_a import A


class B:
    def process(self, item: "A") -> None:
        print(item)
