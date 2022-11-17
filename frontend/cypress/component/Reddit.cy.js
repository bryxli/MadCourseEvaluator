import Reddit from "../../src/components/Reddit";

describe("Reddit", () => {
  it("Rendered", () => {
    cy.mount(<Reddit />);
    cy.get("div").should("have.class", "reddit-box-body");
  });
});
