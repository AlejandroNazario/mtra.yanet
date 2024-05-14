const { gql } = require("apollo-server-express");
//Queries
const typeDefs = gql`
  type Post {
    id: ID
    nombre: String
    apellidos: String
    edad: String
    pais: String 
  }

  type Query {
    mostrar: [Post]
  }
  input PostInput {
    nombre: String
    apellidos: String
    edad:String 
    pais:String
  }
  type Mutation {
    createPost(post: PostInput): Post
    updatePost(id: String, post: PostInput): Post
    deletePost(id: String): String
  }
`;
module.exports = typeDefs;
