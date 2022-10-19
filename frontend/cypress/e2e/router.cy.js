describe('router', () => {
  beforeEach(() => {
    cy.visit('localhost:3000/')
  })
  it('test home page', () => {
    cy.visit('localhost:3000/')
  })
  it('visit course page', () => {
    cy.visit('localhost:3000/course')
  })
  it('visit instructor page', () => {
    cy.visit('localhost:3000/instructor')
  })
})