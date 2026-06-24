from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_b import B


class A:
    def process(self, item: "B") -> None:
        print(item)
