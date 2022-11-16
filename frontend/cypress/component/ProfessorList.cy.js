import ProfessorList from "../../src/components/ProfessorList";

describe("GPAGraph", () => {
  it("Rendered", () => {
    cy.mount(<ProfessorList />);
    // test to see the professor list is mounted,
    // cy.get('div').should('have.class','recharts-wrapper')
  });
});
