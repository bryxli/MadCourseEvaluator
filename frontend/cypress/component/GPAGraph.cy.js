import GPAGraph from "../../src/components/GPAGraph";

describe("GPAGraph", () => {
  it("Rendered", () => {
    cy.mount(<GPAGraph />);
    cy.get("div").should("have.class", "recharts-wrapper");
  });
});
